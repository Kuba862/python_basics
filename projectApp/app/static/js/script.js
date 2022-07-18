const btn = document.getElementById('form_submit_btn');
const firstName =  document.getElementById('id_first_name');
const lastName =  document.getElementById('id_last_name');

function welcome() {
    const p = document.getElementById('welcome_text');
    ((firstName.value == '') || (lastName.value == '')) ? alert('complete data in form') : p.textContent = `Hello ${firstName.value} ${lastName.value}`;
}

btn.addEventListener('click', (e) => {
    e.preventDefault();
    welcome();
});

