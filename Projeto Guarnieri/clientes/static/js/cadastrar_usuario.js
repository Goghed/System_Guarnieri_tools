document.addEventListener("DOMContentLoaded", function() {
    const uploadBtn = document.getElementById('uploadBtn');
    const removeBtn = document.getElementById('removeBtn');
    const fileInput = document.getElementById('id_foto_perfil');
    const profilePhoto = document.getElementById('profilePhoto');

    if (uploadBtn && fileInput) {
        uploadBtn.addEventListener('click', function() {
            fileInput.click();
        });

        fileInput.addEventListener('change', function(event) {
            let reader = new FileReader();
            reader.onload = function(e) {
                profilePhoto.src = e.target.result;
            };
            reader.readAsDataURL(event.target.files[0]);
        });
    }

    if (removeBtn && fileInput) {
        removeBtn.addEventListener('click', function() {
            profilePhoto.src = "/static/images/default-avatar.png"; // Caminho do avatar padrão
            fileInput.value = ""; // Limpa o input de arquivo
        });
    }
});
