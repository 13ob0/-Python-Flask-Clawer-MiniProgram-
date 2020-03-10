

var jumpFlag = true;

Page({

  /**
   * 页面的初始数据
   */
  data: {

    item_notes: [],
    

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

    var that = this;
    
    wx.request({
      url: 'https://www.###.###:5000/notes',
      data: {

      },

      header: {
        'content-type': 'application/json' // 默认值
      },
      success(res) {
        console.log(res.data)
        that.setData({
          item_notes: res.data

        })
      }

    })

  },

  refresh: function(e) {
    wx.showToast({
      title: '正在刷新',
      icon: 'loading',
      duration: 5500
    })

    var that = this;

    wx.request({
      url: 'https://www.###.###:5000/refreshNotes',

      data: {

      },

      header: {
        'content-type': 'application/json' // 默认值
      },
      success(res) {
        
        if (res.data == "刷新成功") {
          wx.showToast({
             title: '刷新成功',
           })
          console.log(res.data)
          that.onLoad();
        }
      }
    })
  },

  detail: function(e) {
    console.log(e);
    if(jumpFlag) {
      jumpFlag = false;
      var id = e.currentTarget.id;
      var temp = JSON.stringify(id);
      wx.navigateTo({
        url: '../detail/detail?num='+temp,
      })
    }
  },


  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    jumpFlag = true;
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  // onPullDownRefresh: function () {

  // },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
    return {
      title: '上课了么-南苑教务信息查询',
      path: '/pages/login/login',
      imageUrl: '../../img/sharing.jpg',
      success: function (res) {
        wx.showToast({
          title: '分享成功',
          icon: 'success'
        })
      }
    }
  },
})