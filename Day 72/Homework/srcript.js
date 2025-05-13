let age = 15;
console.log(age)

const name = "Nikolozi";
console.log(name)

const body = document.getElementById("body")
console.log(body)

function BgChange() {
    body.style.background = "red"
}


const box = document.getElementById("Box")
function BoxChange() {
    box.style.background = "green"
    box.style.width = "400px"
    box.style.height = "400px"
    box.style.transition = "3s"
    box.style.animationTimingFunction = "ease-in-out"
    box.style.borderRadius = "20px"
    box.style.border = "solid 3px yellow"
}