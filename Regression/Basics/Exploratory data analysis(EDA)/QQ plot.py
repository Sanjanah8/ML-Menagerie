# QQ plot to check the normality of the residuals
import statsmodels.api as sm

sm.qqplot(residuals, line ='45')
plt.title('QQ Plot of Residuals')
plt.show()
