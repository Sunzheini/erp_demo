function removeArrow() {
    let allArrows = Array.from(document.querySelectorAll(".fa-arrow-down"))
    let lastArrow = allArrows[allArrows.length - 1]
    lastArrow.remove()
}

removeArrow()
