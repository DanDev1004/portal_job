document.getElementById("departamento").addEventListener("change", function() {
    const departamentoId = this.value;
    fetch(`/ubigeo/obtener-provincias/${departamentoId}/`)
        .then(response => response.json())
        .then(data => {
            const provinciaSelect = document.getElementById("provincia");
            provinciaSelect.innerHTML = '<option value="">Seleccione una provincia</option>';
            data.forEach(provincia => {
                provinciaSelect.innerHTML += `<option value="${provincia.id}">${provincia.nombre}</option>`;
            });
            document.getElementById("distrito").innerHTML = '<option value="">Seleccione un distrito</option>';
        });
});

document.getElementById("provincia").addEventListener("change", function() {
    const provinciaId = this.value;
    fetch(`/ubigeo/obtener-distritos/${provinciaId}/`)
        .then(response => response.json())
        .then(data => {
            const distritoSelect = document.getElementById("distrito");
            distritoSelect.innerHTML = '<option value="">Seleccione un distrito</option>';
            data.forEach(distrito => {
                distritoSelect.innerHTML += `<option value="${distrito.id}">${distrito.nombre}</option>`;
            });
        });
});
