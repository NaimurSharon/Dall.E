import { surprise_me } from "../assets/constant";
import { saveAs } from 'file-saver';

export function getRandomPrompt(prompt){
    const randomIndex = Math.floor(Math.random() * surprise_me.length)
    const randomPromt = surprise_me[randomIndex]
    return randomPromt
}

export async function downloadImage(id,photo){
    saveAs(photo, `download-${id}.jpg`);
}