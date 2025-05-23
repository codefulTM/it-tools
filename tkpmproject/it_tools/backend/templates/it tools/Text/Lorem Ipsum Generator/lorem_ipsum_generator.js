const paragraph = document.getElementById('paragraph');
const paragraphV = document.getElementById('paragraphV');
const sentence = document.getElementById('sentence');
const sentenceV = document.getElementById('sentenceV');
const word = document.getElementById('word');
const wordV = document.getElementById('wordV');
const startWithLoremIpsum = document.getElementById('start-with-lorem');
const asHTML = document.getElementById('as-html');
const textOutput = document.getElementById('text-output');
const generateButton = document.getElementById('generate-text');
const copyButton = document.getElementById('copy-text');

const WORDS = ["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", "sed", "do",
        "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua"];

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

function getRandomWord() {
    return WORDS[Math.floor(Math.random() * WORDS.length)];
}

function generateSentence(wordCount) {
    const words = [];
    for (let i = 0; i < wordCount; i++) {
        words.push(getRandomWord());
    }
    let sentence = words.join(" ");
    return sentence.charAt(0).toUpperCase() + sentence.slice(1) + ".";
}

function generateParagraph(sentencesPerParagraph, wordsPerSentence, startWithLorem) {
    const sentences = [];
    if (startWithLorem) {
        sentences.push("Lorem ipsum dolor sit amet, consectetur adipiscing elit.");
        sentencesPerParagraph -= 1;
    }

    for (let i = 0; i < sentencesPerParagraph; i++) {
        sentences.push(generateSentence(wordsPerSentence));
    }
    return sentences.join(" ");
}

generateButton.addEventListener ('click', () => {
    try {
        const paragraphCount = parseInt(paragraph.value);    
        const sentenceCount = parseInt(sentence.value);
        const wordCount = parseInt(word.value);
        const startWithLoremChecked = startWithLoremIpsum.checked;
        const asHTMLChecked = asHTML.checked;

        let output = "";
        for (let i = 0; i < paragraphCount; i++) {
            const para = generateParagraph(sentenceCount, wordCount, startWithLoremChecked && i === 0);
            output += (asHTMLChecked ? `<p>${para}</p>\\n` : para + "\\n\\n");
        }

        textOutput.value = output.trim();
    } catch (err) {
        console.error('Failed to generate Lorem Ipsum placeholder', err);
        alert('Failed to generate Lorem Ipsum placeholder');
    }
});

copyButton.addEventListener ('click', async () => {
    if (!textOutput || textOutput.value == '') {
        alert('Please generate Lorem Ipsum placeholer first!');
        return;
    }
    try {
        await navigator.clipboard.writeText(textOutput.value);
        alert('Copied Lorem Ipsum placeholder to the clipboard successfully');
    } catch (err) {
        console.error('Failed to copy Loremm Ipsum placeholder to the clipboard');
        alert('Failed to copy Lorem Ipsum placeholder to the clipboard');
    }
});