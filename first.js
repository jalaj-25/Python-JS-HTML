let height = null;
let width = null;

// important: use parentheses
let area = (height ?? 100) * (width ?? 50);

alert(area); // 5000

/*let hour = 12;
let minute = 30;

if (hour == 12 && minute == 30) {
  alert( 'The time is 12:30' );
}

let hour = 12;
let minute = 30;

if (hour == 12 && minute == 30) {
  alert( 'The time is 12:30' );
}

let hour = 9;

if (hour < 10 || hour > 18) {
  alert( 'The office is closed.' );
}

let i = 1;
do{
    console.log("I = ", i);
    i++;
} while(i < 6);*/
