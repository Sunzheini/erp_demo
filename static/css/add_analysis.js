function solve(){
    let position_left = 30
    const INCREMENT = 30
    let place_top_material = 193
    let place_top_machine = 335
    let place_top_position = 475

    let materialCounter = 1
    let machineCounter = 1
    let positionCounter = 1

    // Selections
    let cardDisplayDiv = document.getElementsByClassName('card-display')[0]
    let tableFormMaterials = document.getElementsByClassName('table-form')[2]
    let tableFormMaterialsBody = Array.from(tableFormMaterials.children)[1]
    let tableFormMachines = document.getElementsByClassName('table-form')[3]
    let tableFormMachinesBody = Array.from(tableFormMachines.children)[1]
    let tableFormPositions = document.getElementsByClassName('table-form')[4]
    let tableFormPositionsBody = Array.from(tableFormPositions.children)[1]
    let saveButton = document.getElementsByClassName('form-button')[0]

    // Initially hiding the additional fields
    let allMaterialChildren = Array.from(tableFormMaterialsBody.children)
    let material2Tr = allMaterialChildren[1]
    let material3Tr = allMaterialChildren[2]
    let material4Tr = allMaterialChildren[3]
    let material5Tr = allMaterialChildren[4]
    material2Tr.style.display = 'none'
    material3Tr.style.display = 'none'
    material4Tr.style.display = 'none'
    material5Tr.style.display = 'none'

    let allMachineChildren = Array.from(tableFormMachinesBody.children)
    let machine2Tr = allMachineChildren[1]
    let machine3Tr = allMachineChildren[2]
    let machine4Tr = allMachineChildren[3]
    let machine5Tr = allMachineChildren[4]
    machine2Tr.style.display = 'none'
    machine3Tr.style.display = 'none'
    machine4Tr.style.display = 'none'
    machine5Tr.style.display = 'none'

    let allPositionChildren = Array.from(tableFormPositionsBody.children)
    let position2Tr = allPositionChildren[1]
    let position3Tr = allPositionChildren[2]
    let position4Tr = allPositionChildren[3]
    let position5Tr = allPositionChildren[4]
    position2Tr.style.display = 'none'
    position3Tr.style.display = 'none'
    position4Tr.style.display = 'none'
    position5Tr.style.display = 'none'

    // Adding the + buttons
    const divCardDisplay = document.getElementsByClassName('card-display')[0]
    // 1
    let buttonMaterials = customElements('button', divCardDisplay, null, ['plus-button'], 'buttonMol')
    buttonMaterials.innerHTML += '<i class="fa-solid fa-circle-plus"></i>'
    positionButtons(buttonMaterials, position_left, place_top_material)
    buttonMaterials.addEventListener('click', materialButtonHandler)
    divCardDisplay.appendChild(buttonMaterials)
    // 2
    let buttonAddress = customElements('button', divCardDisplay, null, ['plus-button'], 'buttonAddress')
    buttonAddress.innerHTML += '<i class="fa-solid fa-circle-plus"></i>'
    positionButtons(buttonAddress, position_left, place_top_machine)
    buttonAddress.addEventListener('click', machineButtonHandler)
    divCardDisplay.appendChild(buttonAddress)
    // 3
    let buttonContact = customElements('button', divCardDisplay, null, ['plus-button'], 'buttonContact')
    buttonContact.innerHTML += '<i class="fa-solid fa-circle-plus"></i>'
    positionButtons(buttonContact, position_left, place_top_position)
    buttonContact.addEventListener('click', positionButtonHandler)
    divCardDisplay.appendChild(buttonContact)

    function materialButtonHandler() {
        if (materialCounter < 5) {
            materialCounter += 1

           switch (materialCounter) {
               case 2:
                   material2Tr.style.display = ''
                   break
               case 3:
                   material3Tr.style.display = ''
                   break
               case 4:
                   material4Tr.style.display = ''
                   break
               case 5:
                   material5Tr.style.display = ''
                   break
           }

            place_top_machine += INCREMENT
            positionButtons(buttonAddress, position_left, place_top_machine)
            place_top_position += INCREMENT
            positionButtons(buttonContact, position_left, place_top_position)
        }
    }

    function machineButtonHandler() {
        if (machineCounter < 5) {
            machineCounter += 1

            switch (machineCounter) {
               case 2:
                   machine2Tr.style.display = ''
                   break
               case 3:
                   machine3Tr.style.display = ''
                   break
               case 4:
                   machine4Tr.style.display = ''
                   break
               case 5:
                   machine5Tr.style.display = ''
                   break
           }

            place_top_position += (INCREMENT - 1)
            positionButtons(buttonContact, position_left, place_top_position)
        }
    }

    function positionButtonHandler() {
        if (positionCounter < 5) {
            positionCounter += 1

            switch (positionCounter) {
               case 2:
                   position2Tr.style.display = ''
                   break
               case 3:
                   position3Tr.style.display = ''
                   break
               case 4:
                   position4Tr.style.display = ''
                   break
               case 5:
                   position5Tr.style.display = ''
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
