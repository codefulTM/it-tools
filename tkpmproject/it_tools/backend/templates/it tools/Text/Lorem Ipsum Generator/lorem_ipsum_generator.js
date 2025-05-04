const paragraph = document.getElementById('paragraph');
const paragraphV = document.getElementById('paragraphV');

const sentence = document.getElementById('sentence');
const sentenceV = document.getElementById('sentenceV');

const word = document.getElementById('word');
const wordV = document.getElementById('wordV');

setParagraphValue = ()=>{
    const newValue = Number((paragraph.value - paragraph.min) * 100 / (paragraph.max - paragraph.min));
    const newPosition = 10 - (newValue * 0.2);
    paragraphV.innerHTML = `<span>${paragraph.value}</span>`;
    paragraphV.style.left = `calc(${newValue}% + (${newPosition}px))`;
};
document.addEventListener("DOMContentLoaded", setParagraphValue);
paragraph.addEventListener("input", setParagraphValue);

setSentenceValue = ()=>{
    const newValue = Number((sentence.value - sentence.min) * 100 / (sentence.max - sentence.min));
    const newPosition = 10 - (newValue * 0.2);
    sentenceV.innerHTML = `<span>${sentence.value}</span>`;
    sentenceV.style.left = `calc(${newValue}% + (${newPosition}px))`;
};
document.addEventListener("DOMContentLoaded", setSentenceValue);
sentence.addEventListener("input", setSentenceValue);

setWordValue = ()=>{
    const newValue = Number((word.value - word.min) * 100 / (word.max - word.min));
    const newPosition = 10 - (newValue * 0.2);
    wordV.innerHTML = `<span>${word.value}</span>`;
    wordV.style.left = `calc(${newValue}% + (${newPosition}px))`;
};
document.addEventListener("DOMContentLoaded", setWordValue);
word.addEventListener("input", setWordValue);