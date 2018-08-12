var app = new Vue({
    el:'#app',
    data:{
        list:[
            {
                id:1,
                name:'iphone 8',
                price:6188,
                count:1,
                check:true
            },
            {
                id:2,
                name:'ipod pro',
                price:5888,
                count:1,
                check:true
            },
            {
                id:3,
                name:'mac',
                price:21488,
                count:1,
                check:true
            }
        ]
    },
    computed:{
        totalPrice:function () {
            var total = 0;
            for (var i = 0; i < this.list.length; i++) {
                var item = this.list[i];
                if(item.check){
                    total += item.price * item.count;
                }
            }
            return total.toString().replace(/\B(?=(\d{3})+$)/g,',')
        }
    },
    methods:{
        handleReduce:function(index) {
            if(this.list[index].count === 1) return;
            this.list[index].count--;
        },
        handleAdd:function (index) {
            this.list[index].count++;
        },
        handleRemove:function (index) {
            this.list.splice(index,1);  
        },
        clacPrice:function (index) {
            this.list[index].check = this.list[index].check === true?false:true;
        },
        selectAll:function (choice) {
            for (var i = 0; i < this.list.length; i++) {
                var item = this.list[i];
                item.check = choice;
            }
        }
    }
});