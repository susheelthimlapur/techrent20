/* eslint-env node */
require("@rushstack/eslint-patch/modern-module-resolution")

module.exports = {
  root: true,
  extends: [
    "plugin:vue/vue3-essential",
    "eslint:recommended",
    "plugin:prettier/recommended"
  ],
  parserOptions: {
    ecmaVersion: "latest"
  },
  plugins: ["prettier"],

  rules: {
    "prettier/prettier": "error"
  }
}
