// window.addEventListener("load", solve);

function solve() {
    let position_left = 485
    const INCREMENT = 34
    let position_top_mol = 310
    let position_top_address = 350
    let position_top_contact = 390

    let molCounter = 1
    let addressCounter = 1
    let contactCounter = 1

    // Selections
    let cardDisplayDiv = document.getElementsByClassName('card-display')[0]
    let tableForm = document.getElementsByClassName('table-form')[0]
    let tableFormBody = Array.from(tableForm.children)[0]
    let saveButton = document.getElementsByClassName('form-button')[0]

    // Adding a hidden element
    let newHiddenTr = document.createElement('tr')
    newHiddenTr.textContent = 'empty row'
    newHiddenTr.style.display = 'none'
    tableFormBody.appendChild(newHiddenTr)

    // Hiding the zero input
    const divForRadio = document.getElementById('id_type')
    let divForRadioChildren = Array.from(divForRadio.children)
    let zeroInput = divForRadioChildren[0]
    zeroInput.style.display = 'none'

    // Initially hiding the additional fields
    let allChildren = Array.from(tableFormBody.children)
    let mol2Tr = allChildren[7]
    let mol3Tr = allChildren[8]
    let mol4Tr = allChildren[9]
    let mol5Tr = allChildren[10]
    mol2Tr.style.display = 'none'
    mol3Tr.style.display = 'none'
    mol4Tr.style.display = 'none'
    mol5Tr.style.display = 'none'
    let address2Tr = allChildren[12]
    let address3Tr = allChildren[13]
    let address4Tr = allChildren[14]
    let address5Tr = allChildren[15]
    address2Tr.style.display = 'none'
    address3Tr.style.display = 'none'
    address4Tr.style.display = 'none'
    address5Tr.style.display = 'none'
    let contact2Tr = allChildren[17]
    let contact3Tr = allChildren[18]
    let contact4Tr = allChildren[19]
    let contact5Tr = allChildren[20]
    contact2Tr.style.display = 'none'
    contact3Tr.style.display = 'none'
    contact4Tr.style.display = 'none'
    contact5Tr.style.display = 'none'
    let phone2Tr = allChildren[22]
    let phone3Tr = allChildren[23]
    let phone4Tr = allChildren[24]
    let phone5Tr = allChildren[25]
    phone2Tr.style.display = 'none'
    phone3Tr.style.display = 'none'
    phone4Tr.style.display = 'none'
    phone5Tr.style.display = 'none'
    let email2tr= allChildren[27]
    let email3tr= allChildren[28]
    let email4tr= allChildren[29]
    let email5tr= allChildren[30]
    email2tr.style.display = 'none'
    email3tr.style.display = 'none'
    email4tr.style.display = 'none'
    email5tr.style.display = 'none'

    // Replacing input = file
    let buttonReplacement = customElements(
        'button', cardDisplayDiv, null, ['button-replacement'], null,
        {onclick: "document.getElementsByClassName('file-input')[0].click();" }
    )
    buttonReplacement.innerHTML += '<i class="fa-solid fa-arrow-up-from-bracket"></i>  Избери лого '

    // Adding the + buttons
    const divCardDisplay = document.getElementsByClassName('card-display')[0]
    // 1
    let buttonMol = customElements('button', divCardDisplay, null, ['plus-button'], 'buttonMol')
    buttonMol.innerHTML += '<i class="fa-solid fa-circle-plus"></i>'
    positionButtons(buttonMol, position_left, position_top_mol)
    buttonMol.addEventListener('click', molHandler)
    divCardDisplay.appendChild(buttonMol)
    // 2
    let buttonAddress = customElements('button', divCardDisplay, null, ['plus-button'], 'buttonAddress')
    buttonAddress.innerHTML += '<i class="fa-solid fa-circle-plus"></i>'
    positionButtons(buttonAddress, position_left, position_top_address)
    buttonAddress.addEventListener('click', addressHandler)
    divCardDisplay.appendChild(buttonAddress)
    // 3
    let buttonContact = customElements('button', divCardDisplay, null, ['plus-button'], 'buttonContact')
    buttonContact.innerHTML += '<i class="fa-solid fa-circle-plus"></i>'
    positionButtons(buttonContact, position_left, position_top_contact)
    buttonContact.addEventListener('click', contactHandler)
    divCardDisplay.appendChild(buttonContact)

    function molHandler() {
        if (molCounter < 5) {
            molCounter += 1

           switch (molCounter) {
               case 2:
                   mol2Tr.style.display = ''
                   break
               case 3:
                   mol3Tr.style.display = ''
                   break
               case 4:
                   mol4Tr.style.display = ''
                   break
               case 5:
                   mol5Tr.style.display = ''
                   break
           }

            position_top_address += INCREMENT
            positionButtons(buttonAddress, position_left, position_top_address)
            position_top_contact += INCREMENT
            positionButtons(buttonContact, position_left, position_top_contact)
        }
    }

    function addressHandler() {
        if (addressCounter < 5) {
            addressCounter += 1

            switch (addressCounter) {
               case 2:
                   address2Tr.style.display = ''
                   break
               case 3:
                   address3Tr.style.display = ''
                   break
               case 4:
                   address4Tr.style.display = ''
                   break
               case 5:
                   address5Tr.style.display = ''
                   break
           }

            position_top_contact += (INCREMENT + 12)
            positionButtons(buttonContact, position_left, position_top_contact)
        }
    }

    function contactHandler() {
        if (contactCounter < 5) {
            contactCounter += 1

            switch (contactCounter) {
               case 2:
                   contact2Tr.style.display = ''
                   phone2Tr.style.display = ''
                   email2tr.style.display = ''
                   break
               case 3:
                   contact3Tr.style.display = ''
                   phone3Tr.style.display = ''
                   email3tr.style.display = ''
                   break
               case 4:
                   contact4Tr.style.display = ''
                   phone4Tr.style.display = ''
                   email4tr.style.display = ''
                   break
               case 5:
                   contact5Tr.style.display = ''
                   phone5Tr.style.display = ''
                   email5tr.style.display = ''
                   break
           }
        }
    }

    // Inner functions
    function positionButtons(buttonRef, positionX, positionY) {
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
