function solve() {
    // Selections
    let tableForm = document.getElementsByClassName('table-form')[0]
    let tableFormBody = Array.from(tableForm.children)[0]
    let tableFormBodyElements = Array.from(tableFormBody.children)

    // // Hiding the zero input
    let zeroInputRow = tableFormBodyElements[0]
    let nextRow = tableFormBodyElements[1]
    console.log(zeroInputRow)
    let zeroInput = document.getElementById('id_type')
    // let zeroInputValue = zeroInput.options[zeroInput.selectedIndex].value
    let zeroInputValue = zeroInput.options[zeroInput.selectedIndex].text
    zeroInputRow.style.display = 'none'

    // Replacing
    let newTr = document.createElement('tr')
    newTr.textContent = zeroInputValue
    newTr.style.textAlign = 'center'
    newTr.style.fontWeight = 'bold'
    tableFormBody.insertBefore(newTr, tableFormBodyElements[1]);

    // Hiding empty
    for (let i = 0; i < tableFormBodyElements.length; i++) {
        let currentElement = tableFormBodyElements[i]
        let currentElementChildren = Array.from(currentElement.children)
        let currentElementTd = currentElementChildren[1]
        let currentElementTdChildren = Array.from(currentElementTd.children)
        let currentInput = currentElementTdChildren[0]

        if (currentInput.value === '') {
            currentElement.style.display = 'none'
        }

    }
}

solve()

