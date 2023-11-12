module.exports = {
    content: ["../../templates/**/*.html"],
    theme: {
      extend: {
        fontFamily: {
          'YekanBakh-Light': ['YekanBakh-Light'],
          'YekanBakh-Regular': ['YekanBakh-Regular'],
          'YekanBakh-SemiBold': ['YekanBakh-SemiBold'],
          'YekanBakh-Bold': ['YekanBakh-Bold'],
          'YekanBakh-ExtraBold': ['YekanBakh-ExtraBold'],
          'YekanBakh-ExtraBlack': ['YekanBakh-ExtraBlack'],
        },
      },
    },
    daisyui: {
      themes: ["light"],
    },
    plugins: [require("daisyui")],
  }