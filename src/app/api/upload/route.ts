import { put } from '@vercel/blob';
import { NextResponse } from 'next/server';

export async function POST(request: Request): Promise<NextResponse> {
  try {
    const form = await request.formData();
    const file = form.get('file') as File;
    
    if (!file) {
      return NextResponse.json({ error: 'No file provided' }, { status: 400 });
    }
    
    const blob = await put(file.name, file, { 
      access: 'public',
    });
    
    return NextResponse.json({ url: blob.url });
  } catch (error) {
    console.error("Blob upload error:", error);
    return NextResponse.json({ error: "Failed to upload file to Vercel Blob" }, { status: 500 });
  }
}
