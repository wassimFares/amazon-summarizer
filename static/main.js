form = document.getElementById('form');
result = document.getElementById('result');


form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(form);

    try {
        const response = await fetch('/submit', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            let text = await response.text();
            result.innerHTML = text;
            // let lines = text.split('\n');
            // let positive = []
            // let i = 1
            // for(i; i < lines.length; i++){
            //     if(!lines[i].startsWith('-')){
            //         break;
            //     }
            //     positive.push(lines[i]);
            // }
            // negative_index = i;
            
            // result.innerHTML = `<h1>${lines[0]}</h1><p>${positive.join('<br>')}</p>`
        } else {
            console.error('Form submission failed');
        }
    } catch (error) {
        console.error('Error submitting form:', error);
    }
});