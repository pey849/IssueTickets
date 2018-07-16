// grab the Title input field name from the ticket create page
const titleInput = document.querySelector('input[name=title]');
// grab the slug input field name from the ticket create page
const slugInput = document.querySelector('input[name=slug]');

//we take a value in
const slugify = (val) => {
  //returning a slug that is modified by replacing all the appropriate characters
  //making it lowercase
  return val.toString().toLowerCase().trim()
    .replace(/&/g, '-and-')     //replace & with '-and-'
    .replace(/[\s\W-]+/g, '-')  //replace spaces and non-word chars and dashes with a dash
};

//add a listener on the titleInput which listens for every key up event
titleInput.addEventListener('keyup', (e) => {
  //now it will pass the value on the keyup event to the function we
  //defined above called slugify
  slugInput.setAttribute('value', slugify(titleInput.value));
});
