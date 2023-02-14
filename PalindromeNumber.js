x = 121
let same;
for (let i = 0; i < x.length; i++) {
    if (same === false) {
        return false;
    }
    else if (x[i] === x[x.length - 1 - i]) {
        same = true;
    }
    else {
        same = false;
    }
}
return same;