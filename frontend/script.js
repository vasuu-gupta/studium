const notes_button = document.querySelector(".notes")
const quiz_button = document.querySelector(".quiz")
const flashcards_button = document.querySelector(".flashcards")
const buttons = document.querySelectorAll(".button")

let lastClicked = null

notes_button.addEventListener("click", function() {
    console.log("notes")
})

quiz_button.addEventListener("click", function(){
    console.log("quiz")
})

flashcards_button.addEventListener("click", function(){
    console.log("flashcards")
})

buttons.forEach(button => {button.addEventListener("click", function(){

    if (lastClicked) {
        lastClicked.classList.remove("selected")
    }

    button.classList.add("selected");
    lastClicked = button

})})

buttons.forEach(button => button.addEventListener("mouseenter", function(){
    
}))