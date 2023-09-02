document.addEventListener('DOMContentLoaded', function () {
    const locationForm = document.getElementById('location-form');
    const locationInput = document.getElementById('location-input');
    const needMaterialsCheckbox = document.getElementById('need-materials-checkbox');
    const resultContainer = document.getElementById('result-container');

    locationForm.addEventListener('submit', async function (e) {
        e.preventDefault();
        const placeName = locationInput.value;
        const needMaterials = needMaterialsCheckbox.checked;

        try {
            const response = await fetch(`/api/geocode?placeName=${encodeURIComponent(placeName)}`);
            const data = await response.json();

            if (data.coordinates) {
                const coordinates = data.coordinates;

                if (needMaterials) {
                    const materialsResponse = await fetch(`/api/find-cheap-materials?latitude=${coordinates.latitude}&longitude=${coordinates.longitude}`);
                    const materialsData = await materialsResponse.json();
                    displayMaterialsResult(materialsData);
                } else {
                    const locationsResponse = await fetch(`/api/find-project-locations?latitude=${coordinates.latitude}&longitude=${coordinates.longitude}`);
                    const locationsData = await locationsResponse.json();
                    displayLocationsResult(locationsData);
                }
            } else {
                resultContainer.innerHTML = '<p>Location not found. Please enter a valid location.</p>';
            }
        } catch (error) {
            console.error(error);
            resultContainer.innerHTML = '<p>An error occurred. Please try again later.</p>';
        }
    });

    function displayMaterialsResult(materials) {
        resultContainer.innerHTML = '<h3>Cheap Materials:</h3>';
        if (materials.length > 0) {
            materials.forEach(material => {
                resultContainer.innerHTML += `<p>${material.name}, Cost: ${material.cost}</p>`;
            });
        } else {
            resultContainer.innerHTML += '<p>No cheap materials found in this location.</p>';
        }
    }

    function displayLocationsResult(locations) {
        resultContainer.innerHTML = '<h3>Suitable Project Locations:</h3>';
        if (locations.length > 0) {
            locations.forEach(location => {
                resultContainer.innerHTML += `<p>${location.name}</p>`;
            });
        } else {
            resultContainer.innerHTML += '<p>No suitable project locations found in this location.</p>';
        }
    }
});
