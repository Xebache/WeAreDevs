window.addEventListener("DOMContentLoaded", () => {

  let alert = document.querySelector(".alert")
  let button = document.querySelector(".alert__close")

  if(alert) {
    button.addEventListener('click', () => {
      alert.style.display = 'none'
    })
  }

  let searchForm = document.getElementById('searchForm')
  let pageLinks = document.getElementsByClassName('page-link')
  

  if(searchForm) {
      for(let i = 0; pageLinks.length > i; i++) {
          pageLinks[i].addEventListener('click', function(e){
              e.preventDefault()
              let page = this.dataset.page
              console.log(page)
              searchForm.append(`<input value=${page} name="page" hidden/>`)
              searchForm.submit()
              console.log("click")
          })
      }
  }
})
