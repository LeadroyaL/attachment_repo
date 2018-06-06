直接xposed

input text DDCTF{2517299225169920}

```java
XposedHelpers.findAndHookMethod("cn.chaitin.geektan.crackme.MainActivity", loader, "Joseph", int.class, int.class, new XC_MethodHook() {
    @Override
    protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
        super.beforeHookedMethod(param);
        new Exception().printStackTrace();
        Log.d(TAG, "======== before hook =======");
        Log.d(TAG, "with " + (int) param.args[0] + " and" + (int) param.args[1]);
    }

    @Override
    protected void afterHookedMethod(MethodHookParam param) throws Throwable {
        super.afterHookedMethod(param);
        Log.d(TAG, "======== after hook =======");
        Log.d(TAG, "result is " + param.getResult());
        }
});
```