function edit_organization() {
    let divCardDisplay = document.getElementsByClassName('card-display')[0]
    let tableBody= document.getElementsByTagName('tbody')[0]
    let tableRow = Array.from(tableBody.children)[1]
    let tableD = Array.from(tableRow.children)[1]

    tableD.style.display = 'none'

    let buttonReplacement = customElements(
        'button', divCardDisplay, null, ['button-replacement'], null,
        {onclick: "document.getElementById('id_attachment').click();" }
    )
    buttonReplacement.innerHTML += '<i class="fa-solid fa-arrow-up-from-bracket"></i>  Logo '
    buttonReplacement.style.top = '103px'

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

edit_organization()
