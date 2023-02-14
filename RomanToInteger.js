let s = "III"
let total = 0;
for (let i = 0; i < s.length; i++) {
    if (s[i] === "I") {
        total = total + 1;

    }
    else if (s[i] === "V") {
        if (s[i - 1] === "I") {
            total = total - 2;
        }

        total = total + 5;
    }
    else if (s[i] === "X") {
        if (s[i - 1] === "I") {
            total = total - 2;
        }
        total = total + 10;
    }
    else if (s[i] === "L") {
        if (s[i - 1] === "X") {
            total = total - 20;
        }
        total = total + 50;
    }
    else if (s[i] === "C") {
        if (s[i - 1] === "X") {
            total = total - 20;
        }
        total = total + 100;
    }
    else if (s[i] === "D") {
        if (s[i - 1] === "C") {
            total = total - 200;
        }
        total = total + 500;
    }
    else if (s[i] === "M") {
        if (s[i - 1] === "C") {
            total = total - 200;
        }
        total = total + 1000;
    }
}
return total;
