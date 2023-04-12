// window.addEventListener("load", solve);

function solve() {
    let position_left = 485
    const INCREMENT = 34
    let position_top_mol = 280
    let position_top_address = 320
    let position_top_contact = 360

    let molCounter = 1
    let addressCounter = 1
    let contactCounter = 1
    let anchorIndex = 4

    // Selections
    let tableForm = document.getElementsByClassName('table-form')[0]
    let tableFormBody = Array.from(tableForm.children)[0]
    let saveButton = document.getElementsByClassName('form-button')[0]
    saveButton.addEventListener('click', changeResults)

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

    function changeResults() {
        let molOriginal = document.getElementById('id_mol')
        let addressOriginal = document.getElementById('id_correspondence_address')
        let contactOriginal = document.getElementById('id_contact_person')
        let phoneOriginal = document.getElementById('id_phone')
        let emailOriginal = document.getElementById('id_email')

        // getting from mol * x
        if (document.getElementById('id_mol2')) {
            let mol2Value = document.getElementById('id_mol2').value
            molOriginal.value += '; ' + mol2Value
        }
        if (document.getElementById('id_mol3')) {
            let mol3Value = document.getElementById('id_mol3').value
            molOriginal.value += '; ' + mol3Value
        }
        if (document.getElementById('id_mol4')) {
            let mol4Value = document.getElementById('id_mol4').value
            molOriginal.value += '; ' + mol4Value
        }
        if (document.getElementById('id_mol5')) {
            let mol5Value = document.getElementById('id_mol5').value
            molOriginal.value += '; ' + mol5Value
        }

        // getting from address * x
        if (document.getElementById('id_correspondence_address2')) {
            let address2Value = document.getElementById('id_correspondence_address2').value
            addressOriginal.value += '; ' + address2Value
        }
        if (document.getElementById('id_correspondence_address3')) {
            let address3Value = document.getElementById('id_correspondence_address3').value
            addressOriginal.value += '; ' + address3Value
        }
        if (document.getElementById('id_correspondence_address4')) {
            let address4Value = document.getElementById('id_correspondence_address4').value
            addressOriginal.value += '; ' + address4Value
        }
        if (document.getElementById('id_correspondence_address5')) {
            let address5Value = document.getElementById('id_correspondence_address5').value
            addressOriginal.value += '; ' + address5Value
        }

        // getting from contact * x
        if (document.getElementById('id_contact_person2')) {
            let contact2Value = document.getElementById('id_contact_person2').value
            contactOriginal.value += '; ' + contact2Value
        }
        if (document.getElementById('id_contact_person3')) {
            let contact3Value = document.getElementById('id_contact_person3').value
            contactOriginal.value += '; ' + contact3Value
        }
        if (document.getElementById('id_contact_person4')) {
            let contact4Value = document.getElementById('id_contact_person4').value
            contactOriginal.value += '; ' + contact4Value
        }
        if (document.getElementById('id_contact_person5')) {
            let contact5Value = document.getElementById('id_contact_person6').value
            contactOriginal.value += '; ' + contact5Value
        }

        // getting from phone * x
        if (document.getElementById('id_phone2')) {
            let phone2Value = document.getElementById('id_phone2').value
            phoneOriginal.value += '; ' + phone2Value
        }
        if (document.getElementById('id_phone3')) {
            let phone3Value = document.getElementById('id_phone3').value
            phoneOriginal.value += '; ' + phone3Value
        }
        if (document.getElementById('id_phone4')) {
            let phone4Value = document.getElementById('id_phone4').value
            phoneOriginal.value += '; ' + phone4Value
        }
        if (document.getElementById('id_phone5')) {
            let phone5Value = document.getElementById('id_phone5').value
            phoneOriginal.value += '; ' + phone5Value
        }

        // getting from email * x
        if (document.getElementById('id_email2')) {
            let email2Value = document.getElementById('id_email2').value
            emailOriginal.value += ' ' + email2Value
        }
        if (document.getElementById('id_email3')) {
            let email3Value = document.getElementById('id_email3').value
            emailOriginal.value += ' ' + email3Value
        }
        if (document.getElementById('id_email4')) {
            let email4Value = document.getElementById('id_email4').value
            emailOriginal.value += ' ' + email4Value
        }
        if (document.getElementById('id_email5')) {
            let email5Value = document.getElementById('id_email5').value
            emailOriginal.value += ' ' + email5Value
        }
    }

    function molHandler() {
        if (molCounter < 5) {
            molCounter += 1
            let newTr = document.createElement('tr')
            newTr.innerHTML = `
                <th><label for="id_mol${molCounter}">МОЛ ${molCounter}:</label></th>
                <td><input type="text" name="mol${molCounter}" placeholder="МОЛ ${molCounter}" maxlength="99" required id="id_mol${molCounter}"></td>
                `
            tableFormBody.insertBefore(newTr, tableFormBody.children[anchorIndex+molCounter]);

            position_top_address += INCREMENT
            positionButtons(buttonAddress, position_left, position_top_address)
            position_top_contact += INCREMENT
            positionButtons(buttonContact, position_left, position_top_contact)
        }
    }

    function addressHandler() {
        if (addressCounter < 5) {
            addressCounter += 1
            let newTr = document.createElement('tr')
            newTr.innerHTML = `
                <th><label for="id_correspondence_address${addressCounter}">Адрес за кореспонденция ${addressCounter}:</label></th>
                <td><input type="text" name="correspondence_address${addressCounter}" placeholder="Адрес за кореспонденция ${addressCounter}" maxlength="99" required id="id_correspondence_address${addressCounter}"></td>
                `
            tableFormBody.insertBefore(newTr, tableFormBody.children[anchorIndex+molCounter+addressCounter]);

            position_top_contact += (INCREMENT + 15)
            positionButtons(buttonContact, position_left, position_top_contact)
        }
    }

    function contactHandler() {
        if (contactCounter < 5) {
            contactCounter += 1
            let newTr = document.createElement('tr')
            let newTr1 = document.createElement('tr')
            let newTr2 = document.createElement('tr')
            newTr.innerHTML = `
                <th><label for="id_contact_person${contactCounter}">Лице за контакт ${contactCounter}:</label></th>
                <td><input type="text" name="contact_person${contactCounter}" placeholder="Лице за контакт ${contactCounter}" 
                maxlength="99" required id="id_contact_person${contactCounter}"></td>
                `
            newTr1.innerHTML = `
                <th><label for="id_phone${contactCounter}">Телефон ${contactCounter}:</label></th>
                <td><input type="text" name="phone${contactCounter}" placeholder="Телефон ${contactCounter}" 
                maxlength="20" required id="id_phone${contactCounter}"></td>
                `
            newTr2.innerHTML = `
                <th><label for="id_email${contactCounter}">Имейл ${contactCounter}:</label></th>
                <td><input type="text" name="email${contactCounter}" placeholder="Имейл ${contactCounter}" 
                maxlength="99" required id="id_email${contactCounter}"></td>
                `
            tableFormBody.insertBefore(newTr, tableFormBody.children[Array.from(tableFormBody.children).length]);
            tableFormBody.insertBefore(newTr1, tableFormBody.children[newTr]);
            tableFormBody.insertBefore(newTr2, tableFormBody.children[newTr1]);
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
