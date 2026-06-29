function go(page) {
  window.location.href = page;
}

function logout() {
  localStorage.removeItem("token");
  window.location.href = "login.html";
}

// protect dashboard
if (!localStorage.getItem("token")) {
  window.location.href = "login.html";
}