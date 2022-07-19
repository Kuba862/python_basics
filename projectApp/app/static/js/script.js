const btn = document.getElementById('form_submit_btn');

class Button_status {
    constructor(backgroundColor, color) {
        this.backgroundColor = backgroundColor,
        this.color = color,
        this.button = document.getElementById('form_submit_btn')
    }
    inactive_btn() {
        this.backgroundColor = '#ffafaf';
        this.color = '#fe0000';
        this.button.style.backgroundColor = this.backgroundColor;
        this.button.style.color = this.color;
    }
    active_btn() {
        this.backgroundColor = '#ced';
        this.color = '#00aa80';
        this.button.style.backgroundColor = this.backgroundColor;
        this.button.style.color = this.color;
    }
}
class Form_status {
    constructor() {
        this.inputs = [...document.querySelectorAll('input[type=text]')];
        this.active = false;
    }
    check_form() {
        for(let input of this.inputs) {
            if(input.value == '') {
                const show_status = new Button_status();
                show_status.inactive_btn();
            } else {
                const show_status = new Button_status();
                show_status.active_btn();
                this.active = true;
            }
        }
        if(this.active) {
            const p = document.getElementById('welcome_text');
            p.textContent = `Hello ${this.inputs[0].value} ${this.inputs[1].value}`;       
        }
    }
}
btn.addEventListener('click', (e) => {
    e.preventDefault();
    const form = new Form_status();
    form.check_form();
});

