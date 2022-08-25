like = document.querySelectorAll(".liked");
edit = document.querySelectorAll(".edit");
text_area = document.querySelectorAll(".textarea");
like.forEach((element) => {
  like_handeler(element);
});
edit.forEach((element) => {
  element.addEventListener("click", () => {
    edit_handeler(element);
  });
});
text_area.forEach((element) => {
  element.addEventListener("keyup", (e) => {
    if (e.keyCode == 13 && e.shiftKey) return;
    if (e.keyCode === 13) edit_handeler(element);
  });
});
function like_handeler(element) {
  element.addEventListener("click", () => {
    id = element.getAttribute("data-id");
    is_liked = element.getAttribute("data-is_liked");
    icon = document.querySelector(`#post-like-${id}`);
    count = document.querySelector(`#post-count-${id}`);
    form = new FormData();
    form.append("id", id);
    form.append("is_liked", is_liked);
    fetch("/like/", {
      method: "POST",
      body: form,
    })
      .then((res) => res.json())
      .then((res) => {
        if (res.status == 201) {
          if (res.is_liked === "yes") {
            icon.src = "icon1.png";
            element.setAttribute("data-is_liked", "yes");
          } else {
            icon.src =
              "icon.png";
            element.setAttribute("data-is_liked", "no");
          }
          count.textContent = res.like_count;
        }
      });
  });
}