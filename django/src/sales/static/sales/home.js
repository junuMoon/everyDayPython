const reportBtn = document.getElementById('report-btn')
const img = document.getElementById('img')
const modalBody = document.getElementById('modal-body')

const reportSubmitBtn = document.getElementById('report-save')
const reportForm = document.getElementById('report-form')

if (img){
    reportBtn.classList.remove('not-visible')
}

reportBtn.addEventListener('click', () => {
    console.log('clicked')
    img.setAttribute('class', 'w-100')
    modalBody.prepend(img)

    reportSubmitBtn.addEventListener('click', e=>{
        console.log('clicked2')
        const formData = new FormData()

        // const reportToken = document.getElementsByName('csrfmiddlewaretoken')[0].value
        // const reportName = document.getElementsById('id_name')
        // const reportRemarks = document.getElementsById('id_remarks')

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
            },
            error: function(error){
                console.log(error)
            },
            processData: false,
            contentType: false
        })

    })
})