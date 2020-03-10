// pages/table/table.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    item_class: [],
    listData: {},
    openPicker: false,
    listData: {
      years: ['学年', '2018-2019', '2017-2018', '2016-2017', '2015-2016'],
      terms: ['学期', '1', '2'],
    },

  },

  _sure(e) {
    let data = e.detail
    console.log(JSON.stringify(e.detail[0]))

    var that = this;
    wx.request({
      url: 'https://www.###.###:5000/login/class',
      data: {
        'stuYear': JSON.stringify(e.detail[0]),
        'stuTerm': JSON.stringify(e.detail[1])
      },

      header: {
        'content-type': 'application/json' // 默认值
      },
      success(res) {
        console.log(res.data)
        that.setData({
          item_class: res.data

        })
      }

    })

    if (JSON.stringify(e.detail) === '[]') {
      this.setData({ openPicker: false })
      return
    }
    let { value } = this.data
    value = data.join('')
    this.setData({
      openPicker: false,
      value
    })
    console.log('点击了确定')
  },
  _close(e) {
    console.log(e.detail)
    this.setData({ openPicker: false })
    console.log('点击了取消')
  },
  selTerm() {
    this.setData({ openPicker: true })
  },

  reLogin: function(e){
    wx.redirectTo({
      url: '../login/login',
    })

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

    wx.showToast({
      title: '请选择查询学期',
      icon: 'none'
    })

    var that = this;

    wx.request({
      url: 'https://www.###.###:5000/login/class',
      data: {

      },

      header: {
        'content-type': 'application/json' // 默认值
      },
      success(res) {
        console.log(res.data)
        that.setData({
          item_class: res.data
          
        })
      }

    })

    wx.request({
      url: 'https://www.###.###:5000/refreshNotes',

      data: {

      },

      header: {
        'content-type': 'application/json' // 默认值
      },
      success(res) {
        
        if (res.data == "刷新成功") {
          console.log(res.data)
        }
      }
    })

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