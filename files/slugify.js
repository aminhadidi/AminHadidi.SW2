const titleInput = document.querySelector('input[name=customer_name]')
const slugInput = document.querySelector('input[name=slug]')


const slugify = (val)=>{
  return val.toString().trim()
  .replace(/&/g,'-and-')
  .replace(/[\s\W]+/g,'-')
};
titleInput.addEventListener('keyup',(e)=>{
  slugInput.setAttribute('value',slugify(titleInput.value))
});
