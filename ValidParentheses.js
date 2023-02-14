s = "()"
const openings = [];
for (let i = 0; i < s.length; i++) {
    if (s[i] === '(' || s[i] === '[' || s[i] === '{') {
        openings.push(s[i]);
    } else {
        if (s[i] === ')') {
            if (openings.pop() !== '(') return false;
        } else if (s[i] === ']') {
            if (openings.pop() !== '[') return false;
        } else if (s[i] === '}') {
            if (openings.pop() !== '{') return false;
        }
    }
};

return True && !openings.length;
