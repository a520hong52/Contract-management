	//生成用户数据
    $('#mytable').bootstrapTable({
    	method: 'get',
    	contentType: "application/x-www-form-urlencoded",
    	url:"./getpage",
    	//height:500,//高度调整
    	striped: true, //是否显示行间隔
    	cache:false,
    	pageNumber: 1, //初始化加载第一页，默认第一页
    	pagination:true,//是否分页
    	queryParamsType:'limit',
    	queryParams:queryParams,
    	sidePagination:'server',
		//search: true,   //搜索
		//showRefresh: true, //刷新
		paginationPreText: "上一页",
		paginationNextText: "下一页",
    	pageSize:4,//单页记录数
    	pageList:[4,20,30],//分页步进值
    	clickToSelect: true,//是否启用点击选中行
		toolbar: '#toolbar',
    	toolbarAlign:'left',
    	buttonsAlign:'right',//按钮对齐方式
    	columns:[
        	{
        		title:'全选',
        		field:'select',
        		checkbox:true,
        		width:25,
        		align:'center',
        		valign:'middle'
        	},
        	{
        		title:'ID',
        		field:'ID',
        		visible:false
        	},
        	{
        		title:'合同类型',
        		field:'contract_admin_type',
        		sortable:true
        	},
        	{
        		title:'合同名称',
        		field:'name',
        		sortable:true
        	},
        	{
        		title:'供应商名称',
        		field:'company_name',
        	},
        	{
        		title:'供应商负责人',
        		field:'responsible'
        	},
        	{
        		title:'负责人电话',
        		field:'phone',
        		sortable:true
        	},
        	{
        		title:'职场',
        		field:'contract_admin_workplace',
        	},
        	{
        		title:'合同开始日期',
        		field:'start_date'
        	},
        	{
        		title:'合同结束日期',
        		field:'end_date'
        	},
        	{
        		title:'备注',
        		field:'remark'
        	},
    	],
    	locale:'zh-CN',//中文支持,
    })


    //请求服务数据时所传参数
    function queryParams(params){
    	return{
    		pageSize: params.limit,
    		pageIndex:params.pageNumber,
			typeName:$('#typename').val(),
			workplaceName:$('#workplace_name').val(),
			searchList:$('#search_list').val(),
			searchText:$('#search_text').val()
    	}
    }
	//搜索
	$('#search').click(function(){
		$('#mytable').bootstrapTable('refresh',
			{
				url: './search'

			}
		);
    })

    //删除
    $('#btn_delete').click(function(){
		var ids = $.map($('#mytable').bootstrapTable('getSelections'), function (row) {
			return row.id;
		});
		$.ajax({
			url:'./delete',
			type:'POST',
			traditional:true,
			data:{id:ids},
			success:function(data){
				if (data.status == 'success') {
                    $('#mytable').bootstrapTable('remove', {field: 'id', values: ids});
                }
                else {
					alert(data.status);
				}
			}
		});
    })

    //修改
    $('#btn_edit').click(function(){
		var row = $('#mytable').bootstrapTable('getSelections')
		console.log(row);
		console.log(row[1]);
		if (row.length == 0){
		    alert('请选择需要修改的一行');
            $('#btn_edit').attr("data-target","#");
		}
		else if (row.length == 1){
            $('#btn_edit').attr("data-target","#myModal");
            var name = row.name
            $('#form-field-1').val(row.name)

		}
		else {
            alert('不支持多行的修改');
            $('#btn_edit').attr("data-target","#");
		}
	});