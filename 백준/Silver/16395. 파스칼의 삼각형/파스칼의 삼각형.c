#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>


int ps(int arr[31][31],int n, int k) {

	if (n == k || k == 0) {
		arr[n][k] = 1;
		return arr[n][k];
	}else if (arr[n][k]== 0){
		//비어있다.
		arr[n][k] = ps(arr, n - 1, k - 1) + ps(arr, n - 1, k);
		
	}
	return arr[n][k];
}

int main() {

	int n, k;

	int arr[31][31] = { 0, };

	scanf("%d %d", &n, &k);
	
	printf("%d\n", ps(arr, n-1, k-1));
	
}