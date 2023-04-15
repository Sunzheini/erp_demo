function solve() {
    const theForm = document.getElementsByTagName('form')[0]
    theForm.setAttribute('id', 'create-org-form')

    let theDiv = document.querySelectorAll('form > div')[0]
    let divChildren = Array.from(theDiv.children)

    let newBr1 = document.createElement('br')
    let newBr2 = document.createElement('br')
    let newBr3 = document.createElement('br')

    theDiv.insertBefore(newBr1, divChildren[2]);
    theDiv.insertBefore(newBr2, divChildren[2]);
    theDiv.insertBefore(newBr3, divChildren[8]);

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
