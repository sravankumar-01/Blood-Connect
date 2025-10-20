

let buttons=document.querySelectorAll('.bg-button');
let giveInfo=document.getElementById('giveBloodGroups');
let takeInfo=document.getElementById('takeBloodGroups');


buttons.forEach(button=>{

    button.addEventListener('click',() => {
        buttons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active')
        let give=button.getAttribute('data-give');
        let take=button.getAttribute('data-take');
       
        giveInfo.textContent=give;
        takeInfo.textContent=take;


    }


);
}


);
