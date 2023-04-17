// puts labels and inputs into additional containers (to use later in flex)
// and inserts hrs

function solve() {
    const theForm = document.getElementsByTagName('form')[0]
    theForm.setAttribute('id', 'create-org-form')

    let theDiv = document.querySelectorAll('form > div')[0]
    let divChildren = Array.from(theDiv.children)

    theDiv.innerHTML = ''

    // execution
    let newDivHolder = document.createElement('div')
    newDivHolder.classList.add('table-div-holder', `table-div-holder-1`)
    divChildren[0].classList.add('table-div-label', `table-div-label-1`)
    divChildren[1].classList.add('table-div-input', `table-div-input-1`)
    newDivHolder.appendChild(divChildren[0])
    newDivHolder.appendChild(divChildren[1])
    theDiv.appendChild(newDivHolder)

    let counterDivs = 2
    let counterItems = 2
    for (let i = 2; i < divChildren.length; i+=4) {

        let newDivHolder = document.createElement('div')

        newDivHolder.classList.add('table-div-holder', `table-div-holder-${counterDivs}`)

        divChildren[i].classList.add('table-div-label', `table-div-label-${counterItems}`)
        divChildren[i + 1].classList.add('table-div-input', `table-div-input-${counterItems}`)
        divChildren[i + 2].classList.add('table-div-label', `table-div-label-${counterItems + 1}`)
        divChildren[i + 3].classList.add('table-div-input', `table-div-input-${counterItems + 1}`)

        newDivHolder.appendChild(divChildren[i])
        newDivHolder.appendChild(divChildren[i + 1])
        newDivHolder.appendChild(divChildren[i + 2])
        newDivHolder.appendChild(divChildren[i + 3])

        theDiv.appendChild(newDivHolder)

        counterDivs += 1
        counterItems += 2
    }

    // Insertion of hrs
    // let newBr1 = document.createElement('br')
    // let newBr2 = document.createElement('br')
    // let newBr3 = document.createElement('br')
    // let newBr4 = document.createElement('br')
    //
    // theDiv.insertBefore(newBr1, divChildren[2]);
    // theDiv.insertBefore(newBr2, divChildren[2]);
    // theDiv.insertBefore(newBr3, divChildren[6]);
    // theDiv.insertBefore(newBr4, divChildren[8]);

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
