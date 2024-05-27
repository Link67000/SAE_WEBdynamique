// absences.js
function validerAppel() {
    alert('Appel validé !');
}

// Vous pouvez ajouter des événements ou d'autres fonctions spécifiques ici
document.querySelectorAll('.eleve').forEach(eleve => {
    eleve.addEventListener('click', () => {
        // Logique pour marquer l'élève comme présent ou absent
    });
});
