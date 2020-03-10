
var jumpFlag = true;

Page({

  data: {
    txtUserName: '',
    TextBox2: '',
    code: '',
    src: '',
    filePath: ''
  },

  onLoad: function () {
    this.getCode()
  },

  onShow: function(e) {

    this.getCode()
    
  },

  refresh: function() {
    this.getCode();      
  },

  getCode: function() {
    var timestamp = Date.parse(new Date());
    this.setData({
      src: 'https://www.###.###:5000/getcode?' + timestamp
    });
  },

  inputNum: function(e) {
    console.log(e);
    
    var stuNum = e.detail.value;

    this.setData({
      txtUserName : stuNum
    });

    console.log(this.data.txtUserName);
  },

  inputPw: function (e) {

    var stuPw = e.detail.value;

    this.setData({
      TextBox2: stuPw
    });

    console.log(this.data.TextBox2);
  },  

  inputCode: function (e) {

    var Code = e.detail.value;

    this.setData({
      code: Code
    });

    console.log(this.data.code);
  },

  login: function(e) {
    var that = this;

    wx.request({
      url: 'https://www.###.###:5000/login',
      
      data: {
        'txtUserName': JSON.stringify(this.data.txtUserName),
        'TextBox2': JSON.stringify(this.data.TextBox2),
        'code': JSON.stringify(this.data.code)
      },

      header: {
        'content-type': 'application/json' // 默认值
      },
      success(res) {
        console.log(res.data)
        if(res.data == "登录成功"){
          wx.switchTab({
            url: '../table/table?id=1',
          }
          )
        }
        else {
          console.log("登录失败")
          wx.showToast({
            title: '登录失败\r\n请检查输入重新登录',
            icon: 'none',
            duration: 1700
          })
          jumpFlag = true;
          that.refresh();
        }  
      },
      fail(res) {
        console.log("登录失败")
        wx.showToast({
          title: '登录失败\r\n请检查输入重新登录',
          icon: 'none',
          duration: 1700
        })
        jumpFlag = true;
        that.refresh();
      }
    })

  },

  onShareAppMessage: function () {
    return {
      title: '上课了么-南苑教务信息查询',
      path: '/pages/login/login',
      imageUrl: '../../img/sharing.jpg',
      success: function(res) {
        wx.showToast({
          title: '分享成功',
          icon: 'success'
        })
      }
    }
  },

})
