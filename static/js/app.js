window.addEventListener("DOMContentLoaded", () => {

    // X button on error messages
    let alert = document.querySelector(".alert")
    let button = document.querySelector(".alert__close")
  
    if(alert) {
      button.addEventListener('click', () => {
        alert.style.display = 'none'
      })
    }
  
          
  })
  