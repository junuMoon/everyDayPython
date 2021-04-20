const reportBtn = document.getElementById('report-btn')
const img = document.getElementById('img')
const modalBody = document.getElementById('modal-body')

const reportSubmitBtn = document.getElementById('report-save')
const reportForm = document.getElementById('report-form')
const alertBox = document.getElementById('alert-box')

const handleAlerts = (type, msg) => {
    alertBox.innerHTML = `
        <div class="alert alert-${type}" role="alert">
        ${msg}
        </div>
    `
}

if (img){
    reportBtn.classList.remove('not-visible')
}

reportBtn.addEventListener('click', () => {
    img.setAttribute('class', 'w-100')
    modalBody.prepend(img)

    reportSubmitBtn.addEventListener('click', e=>{
        const formData = new FormData()

        formData.append('csrfmiddlewaretoken', reportForm.csrfmiddlewaretoken.value)
        formData.append('name', reportForm.id_name.value)
        formData.append('remarks', reportForm.id_remarks.value)
        formData.append('image', img.src)


        $.ajax({
            type: 'POST',
            url: '/reports/save',
            data: formData,
            success: function(response){
                console.log(response)
                handleAlerts('success', 'report created')
            },
            error: function(error){
                console.log(error)
                handleAlerts('danger', 'can not create report')
            },
            processData: false,
            contentType: false
        })

    })
})