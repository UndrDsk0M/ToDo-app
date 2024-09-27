"use strict";
const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");
const logInBtn = document.querySelector(".log_in");
const signUpBtn = document.querySelector(".sign_up");
const container = document.querySelector(".container");
const submit = document.querySelectorAll(".submit");
const logInWindow = document.querySelector(".log_in-window");
const signUpWindow = document.querySelector(".sign_up-window");
const closeBtn = document.querySelectorAll(".closeBtn");
const nameInput = document.getElementById("username");
// const lastNameInput = document.getElementById("lastName");
const passwordInput = document.getElementById("password");
function addTask() {
  const list = document.createElement("li");
  list.textContent = taskInput.value;

  list.addEventListener("click", function () {
    list.classList.toggle("completed");
  });

  const deleteButton = document.createElement("button");
  deleteButton.textContent = "√";
  deleteButton.classList.add("done");
  deleteButton.addEventListener("click", function () {
    list.remove();
  });

  list.appendChild(deleteButton);
  taskInput.value ? taskList.appendChild(list) : alert("Fill the input please");

  taskInput.value = "";
}
async function json() {
  // Getting Data
  const nameEl = nameInput.value;
  // const lastName = lastNameInput.value;
  const password = passwordInput.value;
  // Sending data
  const data = {
    name: nameEl,
    password: password,
  };
  const url = "";
  const main = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  return { name: nameEl, passeord: password };
}
function formEn(event) {
  event.preventDefault();
  json();
  // Clear inputs
  nameInput.value = "";
  // lastNameInput.value = "";
  passwordInput.value = "";
}
// submit.forEach((ele) => {
//   ele.addEventListener("click", formEn);
// });
// Event Lesteners
logInBtn.addEventListener("click", () => {
  logInWindow.classList.remove("hide");
  container.style.display = "none";
});
signUpBtn.addEventListener("click", () => {
  signUpWindow.classList.remove("hide");
  container.style.display = "none";
});
closeBtn.forEach((ele) => {
  ele.addEventListener("click", () => {
    logInWindow.classList.add("hide");
    signUpWindow.classList.add("hide");
    container.style.display = "block";
  });
});
document.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    addTask();
  }
});