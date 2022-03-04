let Salary = {
    props : ['salary'],
    template:
    `
        <div>
            Salary template
        
        </div>
    
    `
}


let vm = new Vue({
    el: "#vm",
    data:{
        test: 'test',
    },
    components: {
        'salary' : Salary,
    }
})