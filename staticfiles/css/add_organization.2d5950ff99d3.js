
function solve() {
    // Selections
    let cardDisplayDiv = document.getElementsByClassName('card-display')[0]

    // Replacing input = file
    let buttonReplacement = customElements(
        'button', cardDisplayDiv, null, ['button-replacement'], null,
        {onclick: "document.getElementsByClassName('file-input')[0].click();" }
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

solve()
