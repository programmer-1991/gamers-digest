const editButtons = document.getElementsByClassName("btn-edit");
const contentField = document.getElementById("id_content");
const titleField = document.getElementById("id_title");
const introField = document.getElementById("id_intro");
const topicField = document.getElementById("id_topic")
const postForm = document.getElementById("postForm");
const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the `commentText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 */
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        const slug = e.target.getAttribute("slug");
        const postContent = document.getElementById("content").innerHTML;
        const postTitle = document.getElementById("title").innerText;
        const postIntro = document.getElementById("intro").innerText;
        const postTopic = document.getElementById("topic").getAttribute("topic");


        topicField.value = postTopic;
        introField.value = postIntro;
        titleField.value = postTitle;
        contentField.value = postContent;
        submitButton.innerText = "Update";
        postForm.setAttribute("action", `/edit/${slug}`);
    })};
        /**
         * Initializes deletion functionality for the provided delete buttons.
         * 
         * For each button in the `deleteButtons` collection:
         * - Retrieves the associated comment's ID upon click.
         * - Updates the `deleteConfirm` link's href to point to the 
         * deletion endpoint for the specific comment.
         * - Displays a confirmation modal (`deleteModal`) to prompt 
         * the user for confirmation before deletion.
         */
        for (let button of deleteButtons) {
            button.addEventListener("click", (e) => {
                let slug = e.target.getAttribute("slug");
                deleteConfirm.href = `/delete/${slug}`;
                deleteModal.show();
            })};