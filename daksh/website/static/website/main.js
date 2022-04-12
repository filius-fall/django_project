let Salary = {
    props : ['salary'],
    template:
    `
        <div>


            <form action="/website/expenses/" method="post">
                <label for="expense"></label>
                <input id="expense" name="expense" placeholder="Expenses">

                <label for="des"></label>
                <textarea id="des" name="des" placeholder="Reason for the Expense">
                </textarea>
                <button type="submit" value="submit">Add</button>
            
            </form>
        
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