// window.addEventListener("load", solve);

function solve() {
    let position_left = 485
    let position_top = 245
    const INCREMENT = 38

    let molCounter = 1
    let addressCounter = 1
    let contactCounter = 1

    // Selections
    let tableForm = document.getElementsByClassName('table-form')[0]
    let tableFormBody = Array.from(tableForm.children)[0]

    // Hiding the zero input
    const divForRadio = document.getElementById('id_type')
    let divForRadioChildren = Array.from(divForRadio.children)
    let zeroInput = divForRadioChildren[0]
    zeroInput.style.display = 'none'

    // Adding the + buttons
    const divCardDisplay = document.getElementsByClassName('card-display')[0]

    // 1
    position_top += INCREMENT
    let buttonMol = customElements('button', divCardDisplay, null, ['plus-button'], 'buttonMol')
    positionButtons(buttonMol, position_left, position_top)
    buttonMol.addEventListener('click', molHandler)
    divCardDisplay.appendChild(buttonMol)

    // 2
    position_top += INCREMENT
    let buttonAddress = customElements('button', divCardDisplay, null, ['plus-button'], 'buttonAddress')
    positionButtons(buttonAddress, position_left, position_top)
    buttonAddress.addEventListener('click', addressHandler)
    divCardDisplay.appendChild(buttonAddress)

    // 3
    position_top += INCREMENT
    let buttonContact = customElements('button', divCardDisplay, null, ['plus-button'], 'buttonContact')
    positionButtons(buttonContact, position_left, position_top)
    buttonContact.addEventListener('click', contactHandler)
    divCardDisplay.appendChild(buttonContact)

    function molHandler() {
        molCounter += 1
        let anchorIndex = 4
        let newTr = document.createElement('tr')
        newTr.innerHTML = `
            <th><label for="id_mol${molCounter}">МОЛ${molCounter}:</label></th>
            <td><input type="text" name="mol${molCounter}" placeholder="МОЛ${molCounter}" maxlength="99" required id="id_mol${molCounter}"></td>
            `
        tableFormBody.insertBefore(newTr, tableFormBody.children[anchorIndex+molCounter]);
    }

    function addressHandler() {

    }

    function contactHandler() {

    }



    // Inner functions
    function positionButtons(buttonRef, positionX, positionY) {
        buttonRef.innerHTML += '<i class="fa-solid fa-circle-plus"></i>'
        buttonRef.style.left = `${positionX}px`
        buttonRef.style.top = `${positionY}px`
    }

    function customElements(type, parentNode, content, classes, id, attributes, useInnerHtml) {
        const htmlElement = document.createElement(type)
        if (content && useInnerHtml) {
            htmlElement.innerHTML = content
        } else {
            if (content && type !== 'input') {
                htmlElement.textContent = content
            }
            if (content && type === 'input') {
                htmlElement.value = content
            }
        }
        if (classes && classes.length > 0) {
            htmlElement.classList.add(...classes)
        }
        if (id) {
            htmlElement.id = id
        }
        // {src: 'link', href: 'http'}
        if (attributes) {
            for (const key in attributes) {
                htmlElement.setAttribute(key, attributes[key])
                // htmlElement[key] = attributes[key] // option2
            }
        }
        if (parentNode) {
            parentNode.appendChild(htmlElement)
        }
        return htmlElement
    }
}

solve()
