let s = "()"
const openings = [];
for (const element of s) {
    if (element === '(' || element === '[' || element === '{') {
        openings.push(element);
    } else {
        if (element === ')') {
            if (openings.pop() !== '(') return false;
        } else if (element === ']') {
            if (openings.pop() !== '[') return false;
        } else if (element === '}') {
            if (openings.pop() !== '{') return false;
        }
    }
};

return True && !openings.length;
