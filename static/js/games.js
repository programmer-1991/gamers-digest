// buttons
const editButtons = document.getElementsByClassName("btn-edit")
const deleteButtons = document.getElementsByClassName("btn-delete")
const submitButton = document.getElementById("submit_button")

// form
const formCard = document.getElementById("form_card")
const gameForm = document.getElementById("form")

// fields
const titleField = document.getElementById("id_title")
const descriptionField = document.getElementById("id_description")
const genreField = document.getElementById("id_genre")
const platformField = document.getElementById("id_platform")
const ageratingField = document.getElementById("id_age_rating")
const developerField = document.getElementById("id_developer")
const publisherField = document.getElementById("id_publisher")
const releaseField = document.getElementById("id_release")


// deletion action
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"))
const deleteConfirm = document.getElementById("deleteConfirm")

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        const slug = e.target.getAttribute("slug");
        const title = document.getElementById("title").innerText
        const description = document.getElementById("description").innerHTML
        const genre = document.getElementById("genre").innerText
        const platform = document.getElementById("platform").getAttribute("data-id")
        const ageRating = document.getElementById("age").innerText
        const developer = document.getElementById("developer").innerText
        const publisher = document.getElementById("publisher").innerText
        const release = document.getElementById("release").innerText
    
        titleField.value = title
        descriptionField.value = description;
        genreField.value = genre;
        platformField.value = platform
        ageratingField.value = ageRating
        developerField.value = developer
        publisherField.value = publisher
        releaseField.value = release

        submitButton.innerText = "Update"
        formCard.style.display = "block"
        formCard.scrollIntoView()
        gameForm.setAttribute("action", `/edit/game/${slug}/`)

    })
}

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let slug = e.target.getAttribute("slug")
        deleteConfirm.href = `/delete/game/${slug}`
        deleteModal.show()
    })
}