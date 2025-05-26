// 1
for (let i = 1; i <= 10; i++) {
    console.log(i);
}

//2
console.log("-------------------------------------------")
for (let i = 1; i <= 50; i++) {
  if (i % 2 === 0) {
    console.log(i + " ლუწია");
  } else {
    console.log(i + " კენტია");
  }
}

//3
console.log("------------------------------------------")
let number = prompt("შეიყვანე რიცხვი გამრავლების ცხრილისთვის:");

number = Number(number);

for (let i = 1; i <= 10; i++) {
  let result = number * i;
  console.log(number + " x " + i + " = " + result);
}

//4
console.log("------------------------------------------")
